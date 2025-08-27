<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import { useTheme } from 'vuetify'

const theme = useTheme()
</script>

<template>
  <v-app>
    <v-main>
      <header>
        <div class="wrapper">
          <v-btn @click="theme.toggle()" text="Toggle Light / Dark"></v-btn>
          <nav>
            <RouterLink to="/">Home</RouterLink>
          </nav>
        </div>
      </header>

      <RouterView />
    </v-main>
  </v-app>
</template>

<style scoped></style>
