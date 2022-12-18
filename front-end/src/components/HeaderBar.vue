<template>
  <v-app-bar app color="#aaaaaa" dark flat class="px-8">
    <v-btn icon>
        <v-icon color="#e1f223">fa-user</v-icon>
    </v-btn>
    <div v-if="isLogin">
        <p>ログイン中</p>
    </div>
    <div v-else>ゲスト</div>
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
  methods:{}
}
  
</script>

<style>

</style>