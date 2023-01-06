

<template>

    <div class= "cpnt" v-if="!adminMode">

        <label for="login">Mot de passe </label>
        <input type="password" v-model="pwd"/>
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



export default {
    name: "Login",

    data(){
        let adminMode = false;
        return(adminMode);
    },
    methods: {
        async login(pwd){
            let response = await QuizApiService.postLogin(pwd);
            if (response.status === 200){
                window.localStorage.setItem("token", response.data["token"]);
                this.adminMode = true;

                console.log(this.adminMode);
            }
        }
    },
    computed: {
        isToken(){
            let token = window.localStorage.getItem("token");
            console.log("aaaa")
            return (token === null ? true : false);
        }
    }
        
    
}
</script>

