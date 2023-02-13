<!-- https://qiita.com/sand/items/4b3e222dbb9315e2b0c0#3-vue%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%A0 -->
<template>
  <v-app>
    <v-card width="400" class="mx-auto mt-5">
      <v-card-title class="text-center">{{ title }}</v-card-title>
      <v-form class="centering-wmargin">
        <v-text-field
          variant="outlined"
          density="comfortable"
          prepend-icon="mdi-alphabet-latin"
          label="英単語"
          v-model="word"
        />
        <v-text-field
          variant="outlined"
          density="comfortable"
          prepend-icon="mdi-ideogram-cjk-variant"
          label="意味"
          v-model="meaning"
        />
        <v-text-field
          variant="outlined"
          density="comfortable"
          prepend-icon="mdi-format-list-bulleted-type"
          label="レベル"
          v-model="level"
        />
        <!-- <v-text-field
          variant="outlined"
          density="comfortable"
          prepend-icon="mdi-lock"
          label="レベル"
          v-model="password"
        /> -->
        <v-card-text class="text-center" style="color: red">
          <h3>
            {{ errormessage }}
          </h3></v-card-text
        >
        <v-card-actions class="justify-center">
          <v-btn
            variant="outlined"
            @click="doRegister"
            v-bind:disabled="activateSubmit"
            >Register</v-btn
          >
        </v-card-actions>
      </v-form>
      <!-- <p>Current token = {{ token }}</p> -->
    </v-card>
  </v-app>
</template>

<script>
// import { inject } from 'vue'
import axios from "axios";

export default {
  data() {
    return {
      title: "Register",
      word: "",
      meaning: "",
      level: "",
      owner_id: -1,
      username: "",
      errormessage: "",
    };
  },
  methods: {
    doRegister: function () {
      console.log(this.owner_id);
      const params = {
        English_word: this.word,
        Japanese_word: this.meaning,
        level: this.level,
        owner_id: this.owner_id,
      };
      // console.log("doSignup:: username=", this.username, " passowrd=", this.password)
      // const params = {
      //     // "email": this.email,
      //     "username": this.username,
      //     "password": this.password
      // }
      // if (this.password === this.password2) {
      //     let config = {
      //         headers: {
      //             'Content-Type': 'application/json'
      //         }
      //     };
      //     const URL = 'http://localhost:8000/users/'
      //     axios.post(URL, params, config)
      //         .then((response) => {
      //             console.log("response.data = ", response.data)
      //             this.token = response.data.access_token
      //             localStorage.setItem('token', response.data.access_token);
      //             this.$emit('change-login', true)
      //             this.$router.push({
      //                 name: 'home',
      //             })
      //         })
      //         .catch((err) => {
      //             console.log("Error = ", err)
      //         })
      // } else {
      //     this.errormessage = "two passwords do not match"
      // }
    },
  },
  mounted: function () {
    const token = String(localStorage.token);
    const URL = "http://127.0.0.1:8000/users/me";
    console.log(token);
    let config = {
      headers: {
        "Content-Type": "application/json",
        Authorization: "Bearer " + token,
      },
    };
    axios
      .get(URL, config)
      .then((response) => {
        console.log("response.data = ", response.data);
        // 下がtypescriptの型チェックでエラーになります。助けてください。
        // eslint-disable-next-line
        //@ts-ignore
        this.owner_id = response.data.id;
        this.username = response.data.username;
      })
      .catch((err) => {
        this.errormessage = "ログインしてください";
      });
  },
  computed: {
    activateSubmit() {
      console.log(this.username);
      if (this.username == "") {
        return true;
      } else {
        return false;
      }
    },
  },
};
</script>

<style scoped>
.centering-wmargin {
  margin: 15px;
}
</style>
