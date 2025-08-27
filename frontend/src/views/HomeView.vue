<script setup lang="ts">
import axios from 'axios'
import CrackedKey from '@/components/CrackedKey.vue'

axios.defaults.baseURL = 'http://localhost:8000'

const isFormValid = defineModel('isFormValid', { default: false })
const normalCipherText = defineModel('normalCipherText', { default: '' })
const faultyCipherText = defineModel('faultCipherText', { default: '' })
const loading = defineModel('loading', { default: false })
const status = defineModel('status', { default: '' })
const error = defineModel('error', { default: '' })
const keys = defineModel('keys', { default: [] })
const cipherTextRules = [
  (value: string) => (/^[0-9a-f]{32}$/.test(value) ? true : 'Cipher text must be 32 hex chars'),
]

async function submit() {
  loading.value = true
  status.value = ''
  error.value = ''
  keys.value = []

  let response
  let taskStatus
  try {
    response = await axios.post('/tasks', {
      normalCipherText: normalCipherText.value,
      faultyCipherText: faultyCipherText.value,
    })
  } catch {
    error.value = 'Failed to send your ciphertext to computation. Please try again.'
    return
  }
  if (response.status != 201) {
    error.value = `Status code ${response.status}`
  }
  const taskId = response.data['taskId']
  while (true) {
    try {
      response = await axios.get(`/tasks/${taskId}`)
    } catch {
      error.value = 'Failed to fetch your task result. Please try again.'
      return
    }
    taskStatus = response.data.taskStatus
    if (taskStatus === 'PENDING') {
      status.value = 'Your task is currently waiting. Processing will start soon.'
    } else if (taskStatus === 'STARTED') {
      status.value = 'Your task has started, it should be completed in one minute.'
    } else if (response.data.taskStatus === 'RETRY') {
      status.value = 'Your task is being retried.'
    } else if (response.data.taskStatus === 'SUCCESS') {
      status.value = 'Computation successful.'
      keys.value = response.data.taskResult
      break
    } else if (response.data.taskStatus === 'ERROR') {
      error.value = 'Something went wrong. Please investigate.'
      break
    }
    await new Promise((r) => setTimeout(r, 1000))
  }
  loading.value = false
}
</script>

<template>
  <main>
    <v-form v-model="isFormValid" @submit.prevent="submit">
      <v-text-field
        v-model="normalCipherText"
        :rules="cipherTextRules"
        label="Normal cipher text"
        required
      ></v-text-field>
      <v-text-field
        v-model="faultyCipherText"
        :rules="cipherTextRules"
        label="Faulty cipher text"
        required
      ></v-text-field>
      <v-btn
        :disabled="!isFormValid"
        :loading="loading"
        class="mt-2"
        text="Submit"
        type="submit"
        block
      ></v-btn>
    </v-form>
    <div v-if="error">
      {{ error }}
    </div>
    <div v-if="status">
      {{ status }}
    </div>
    <CrackedKey v-for="crackedKey in keys" :key="crackedKey" :crackedKey="crackedKey" />
  </main>
</template>
