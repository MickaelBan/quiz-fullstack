

<template>

    <div class="cpnt" v-if="!adminMode">

        <label for="login">Mot de passe </label>
        <input type="password" v-model="pwd" />
        <input type="submit" name="login" value="Connexion" v-on:click="login(pwd)">
    </div>

    <div id="back-office" v-else>
        <p>Bien joué bg</p>
    </div>

</template>

<style>

</style>

<script>
import QuizApiService from "../services/QuizApiService";
import AdminStorageService from "../services/AdminStorageService"


export default {
    name: "Login",

    data() {
        let adminMode = false;
        let pwd = ""
        return { adminMode, pwd };
    },
    methods: {
        async login(pwd) {
            let response = await QuizApiService.postLogin(pwd);
            if (response.status === 200) {
                AdminStorageService.saveToken(response.data["token"]);
                this.adminMode = true;

                console.log(this.adminMode);
            }
        }
    },
    computed: {
        isToken() {
            let token = AdminStorageService.getToken("token");
            console.log("aaaa")
            return (token === null ? true : false);
        }
    }


}
</script>

