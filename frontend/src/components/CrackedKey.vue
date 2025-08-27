<script setup lang="ts">
const props = defineProps<{ crackedKey: string }>()
const copyKey = () => {
  navigator.clipboard.writeText(props.crackedKey)
}
</script>

<template>
  <v-text-field
    append-inner-icon="mdi-content-copy"
    @click:append-inner="copyKey"
    class="crackedKey"
    >{{ props.crackedKey }}</v-text-field
  >
</template>

<style scoped>
.crackedKey {
  width: 400px;
}
</style>
