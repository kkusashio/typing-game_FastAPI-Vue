<template>
    <v-navigation-drawer v-model="drawer">
    <v-sheet color="grey-lighten-4" class="pa-4">
      <v-avatar class="mb-4" color="primary" size="64">
        <span class="white--text text-h5">{{ username[0] }}</span>
      </v-avatar>
  
      <div>{{username}}</div>
    </v-sheet>
  
    <v-divider></v-divider>
  
    <v-list>
      <v-list-item v-for="[icon, text, link] in links" :key="icon" link>
        <template v-slot:prepend>
          <v-icon>{{ icon }}</v-icon>
        </template>
        <a v-bind:href="link" class="black">
          <v-list-item-title to=''>{{ text }}</v-list-item-title>
        </a>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
  <v-app-bar app color="#aaaaaa" dark flat class="px-8">
    <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
    <!-- <v-btn icon>
        <v-icon color="#e1f223">fa-user</v-icon>
    </v-btn> -->
    <div v-if="isLogin" style="margin-left:20px">
        <p>{{username}}</p>
    </div>
    <div style="margin-left:20px" v-else><h3 class="font-weight-medium">Guest</h3></div>
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
    <v-btn to="/" icon>
      <v-icon size="20">mdi-home</v-icon>
    </v-btn>
  </v-app-bar>
</template>

<script lang="ts">
import axios from "axios";

export default{
  props:['isLogin'],
  data() {
    return {
      drawer: false,
      username: "Guest User",
      links: [
        ['mdi-home', 'Home', '/'],
        ['mdi-account-group', 'Login','/user'],
        ['mdi-alphabetical-variant', 'English','/about']
      ],
    }
  },
  watch: {
    isLogin:function(){
      const token = String(localStorage.token);
      const URL = 'http://127.0.0.1:8000/users/me'
      console.log(token)
      let config = {
        headers: {
          'Content-Type': 'application/json',
          Authorization:'Bearer '+token,
        }
      };
      axios.get(URL, config)
        .then((response) => {
          console.log("response.data = ", response.data)
          // 下がtypescriptの型チェックでエラーになります。助けてください。
          // eslint-disable-next-line 
          //@ts-ignore
          this.username=response.data.username

        })
        .catch((err) => {
          console.log("Error = ", err)
        })
    }
    
  },
}
  
</script>

<style>
a.black {
  text-decoration: none;
  color: #000;
}
</style>