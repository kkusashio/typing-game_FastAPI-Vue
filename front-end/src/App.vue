<template>
  <v-app>
      
        <Header v-bind:isLogin="isLogin" />
        <v-main>
            <router-view v-on:change-login="changeLogin" />
        </v-main>
        <Footer v-bind:isLogin="isLogin" />
  </v-app>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import Header from './components/HeaderBar.vue'
import Footer from './components/FooterBar.vue'

export default defineComponent({
  name: 'App',
  components: {
    Header,
    Footer
  },
  data() {
    return {
      isLogin: (String(localStorage.token).length)>1
    }
  },
  methods: {
    changeLogin: function (val:boolean) {
      this.isLogin = val
    }
  },
})
</script>
<style scoped>

</style>