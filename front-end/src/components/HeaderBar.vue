<template>
  <v-navigation-drawer v-model="drawer" app>
    <p>ここはdrawer領域</p>
    <p>スマホ用なのか？</p>
  </v-navigation-drawer>
  <v-app-bar app color="#aaaaaa" dark flat class="px-8">
    <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
    <!-- <v-btn icon>
        <v-icon color="#e1f223">fa-user</v-icon>
    </v-btn> -->
    <div v-if="isLogin" style="margin-left:20px">
        <p>ログイン中</p>
    </div>
    <div style="margin-left:20px" v-else>Guest</div>
    <v-spacer></v-spacer>
    <v-btn icon>
      <v-icon size="20">mdi-application-brackets</v-icon>
    </v-btn>
    
    <v-btn to="/logout" icon v-if="isLogin">
      <v-icon size="20">mdi-logout-variant</v-icon>
    </v-btn>
    <v-btn to="/user" icon v-else>
      <v-icon size="20">mdi-account-group</v-icon>
    </v-btn>
    <v-divider vertical class="mx-md-5 mx-2"/>
    <v-btn to="/about" icon>
      <v-icon size="20">mdi-home</v-icon>
    </v-btn>
  </v-app-bar>
</template>

<script lang="ts">
export default {
  props:['isLogin'],
  methods: {},
  data: () => ({ drawer: null }),
}
  
</script>

<style>

</style>