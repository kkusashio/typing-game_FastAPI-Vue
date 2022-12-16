<template>
    <div class="app">
      <p>{{ name }} - {{ age }}</p>
      <v-btn>hello</v-btn>
      <button @click="changeName('changed')">change name</button>
      <button @click="changeAge('30')">change age</button>
    </div>
  </template>
  
  <script lang="ts">
  import { defineComponent } from 'vue';
  
  export default defineComponent({
    name: "HomeView",
    components: {},
    data() {
      return {
        name: 'Link',
        age: 25 as number | string
      }
    },
    methods: {
    changeName(name: string){
      this.name = name
    },
    changeAge(age: string | number){
      this.age = age
    }
  }
});
</script>

<style>
</style>