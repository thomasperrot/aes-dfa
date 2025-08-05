<script setup lang="ts">
import { ref } from 'vue'
import axios from 'axios';

axios.defaults.baseURL = 'http://localhost:8000';

const isFormValid = defineModel("isFormValid")
const normalCipherText = defineModel("normalCipherText")
const faultyCipherText = defineModel("faultCipherText")
const loading = defineModel("loading")
const status = defineModel("status")
const error = defineModel("error")
const keys = defineModel("keys")
const cipherTextRules = [value => /^[0-9a-f]{32}$/.test(value) ? true : 'Cipher text must be 32 hex chars']

async function submit (event) {
 loading.value = true
 status.value = ""
 error.value = ""
 keys.value = []

 let response
 let taskStatus
 try {
   response = await axios.post("/tasks", {normalCipherText: normalCipherText.value,  faultyCipherText: faultyCipherText.value})
 } catch {
   error.value = "Failed to send your ciphertext to computation. Please try again."
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
     error.value = "Failed to fetch your task result. Please try again."
     return
   }
   taskStatus = response.data.taskStatus
   if (taskStatus === "PENDING") {
      status.value = "Your task is currently waiting. Processing will start soon."
   } else if (taskStatus === "STARTED") {
      status.value = "Your task has started, it should be completed in one minute."
   } else if (response.data.taskStatus === "RETRY") {
      status.value = "Your task is being retried."
   } else if (response.data.taskStatus === "SUCCESS") {
      status.value = "Computation successful."
      keys.value = response.data.taskResult
      break
   } else if (response.data.taskStatus === "ERROR") {
     error.value = "Something went wrong. Please investigate."
     break
   }
   await new Promise(r => setTimeout(r, 1000));
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
    <div v-for="key in keys">
      {{ key }}
    </div>
  </main>
</template>
