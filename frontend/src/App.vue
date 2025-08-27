<script setup lang="ts">
import { useTheme } from 'vuetify'
import HomeView from './views/HomeView.vue'

const theme = useTheme()
</script>

<template>
  <v-app>
    <v-main>
      <header>
        <div class="wrapper">
          <v-btn @click="theme.toggle()" text="Toggle Light / Dark"></v-btn>
        </div>
      </header>
      <HomeView />
    </v-main>
  </v-app>
</template>

<style scoped></style>
