

<template>

    <div class="cpnt" v-if="!adminMode">
        <label for="login">Mot de passe </label>
        <input type="password" id="login" v-model="pwd" />
        <div class="red"><label v-if="!goodPassword">Password incorrect</label></div>
        <input type="submit" name="login" value="Connexion" v-on:click="login(pwd)">

    </div>

    <div id="back-office" v-else>
        <div class="button">
            <input type="submit" value="list of questions" v-on:click="$router.push({ name: 'DataList' })">
        </div>
    </div>

</template>

<style>

</style>

<script>
import QuizApiService from "../services/QuizApiService";
import AdminStorageService from "../services/AdminStorageService"


export default {
    name: "Login",
    components: {
        AdminStorageService
    },
    data() {
        let adminMode = false;
        let pwd = ""
        let goodPassword = true
        return { adminMode, pwd, goodPassword };
    },
    created() {
        this.adminMode = AdminStorageService.isAdmin();
    },
    methods: {
        async login(pwd) {
            let response = await QuizApiService.postLogin(pwd);
            if (response !== undefined) {
                if (response.status === 200) {
                    AdminStorageService.saveToken(response.data["token"]);
                    this.adminMode = AdminStorageService.isAdmin();

                    console.log(this.adminMode);
                }
            }
            else {
                this.goodPassword = false
            }
        }
    }
}
</script>

