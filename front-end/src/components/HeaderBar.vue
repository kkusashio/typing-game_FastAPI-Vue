<template>
  <v-navigation-drawer v-model="drawer" app>
    <p>ここはdrawer領域</p>
    <p>スマホ用なのか？</p>
    <v-card>
      <div class="mxxxx">
        <v-icon size="30">mdi-account-group</v-icon>
        <router-link to="/user">
          <span class="pagetag">Login</span>
        </router-link>
      </div>
        
    </v-card>
    
  </v-navigation-drawer>
  <v-app-bar app color="#aaaaaa" dark flat class="px-8">
    <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
    <!-- <v-btn icon>
        <v-icon color="#e1f223">fa-user</v-icon>
    </v-btn> -->
    <div v-if="isLogin" style="margin-left:20px">
        <p>{{username}}</p>
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
import axios from "axios";

export default{
  props:['isLogin'],
  data() {
    return {
      drawer: false,
      username: ""
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
.mxxxx {
  margin-top: 10px;
  margin-bottom: 10px;
}
.pagetag{
  margin-left: 80px;
  font-size:large;
}
a {
  text-decoration: none;
  color: #000;
}
</style>