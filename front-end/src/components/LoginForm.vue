<!-- https://qiita.com/sand/items/4b3e222dbb9315e2b0c0#3-vue%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%A0 -->
<template>
    <v-app>
        <v-card width="400" class="mx-auto mt-5">
            <v-card-title class="text-center">{{ title }}</v-card-title>
            <v-card-text class="text-center">
                <span class="text-center">Not registered yet ? </span>
                <a href="http://localhost:8080/signup">signup</a>
            </v-card-text>
            <v-form class="centering-wmargin">
                <v-text-field variant="outlined" density="comfortable" prepend-icon="mdi-account-circle"
                    label="username" v-model="username" />
                <v-text-field v-bind:type="showPassword ? 'text' : 'password'" variant="outlined" density="comfortable"
                    prepend-icon="mdi-lock" v-bind:append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
                    label="password" @click:append="showPassword = !showPassword" v-model="password" />
                <v-card-text class="text-center" style="color:red">{{ errorMessage }}</v-card-text>
                <!-- <p>{{ errorMessage }}</p> -->
                <v-card-actions class="justify-center">
                    <v-btn variant="outlined" @click="doLogin">Login</v-btn>
                </v-card-actions>
            </v-form>
            <!-- <p>Current token = {{ token }}</p> -->
        </v-card>
    </v-app>
</template>

<script>
// import { inject } from 'vue'
import axios from 'axios'

export default {
    data() {
        return {
            title: "Login",
            token: "",
            showPassword: false,
            username: "",
            password: "",
            errorMessage:""
        }
    },
    methods: {
        doLogin: function () {
            console.log("doLogin:: username=", this.username, " passowrd=", this.password)
            const params = new URLSearchParams();
            params.append('username', this.username);    // 渡したいデータ分だけappendする
            params.append('password', this.password);
            let config = {
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                }
            };
            const URL = 'http://localhost:8000/token'
            axios.post(URL, params, config)
                .then((response) => {
                    console.log("response.data = ", response.data)
                    this.token = response.data.access_token
                    localStorage.setItem('token', response.data.access_token);
                    this.$emit('change-login', true)
                    this.$router.push({
                        name:'home',
                    })
                })
                .catch((err) => {
                    this.errorMessage = "Incorrect username or password"
                    console.log(err)
                })
        }
    }

}
</script>

<style scoped>
.centering-wmargin {
    margin: 15px;
}
</style>