<script setup>
import { ref, onMounted } from "vue";

const message = ref(""); 

const printDataframe = async () => {
  if (window.pywebview) {
    const response = await window.pywebview.api.get_data(); // Access backend API function
    message.value = response; 
  } else {
    message.value = "Pywebview API not available."; // Hello
  }
};

onMounted(() => {
  printDataframe();
});
</script>

<template>
  <div>
    <h1>Pywebview + Nuxt.js</h1>
    <p>{{ message }}</p>
  </div>
</template>
