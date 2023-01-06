<template>
    <QuestionDisplay :question=question :adminMode=true />

    <div class="button" id="edit">
        <input type="submit" value="Editer la question"
            v-on:click="$router.push({ name: 'EditQuestion', params: { id: question.id } })">
    </div>
    <div class="button" id="delete">
        <input type="submit" value="Supprimer la question" v-on:click="deleteQuestion">
    </div>



</template>



<script>
import AdminStorageService from '../services/AdminStorageService';
import QuizApiService from '../services/QuizApiService';
import QuestionDisplay from './QuestionDisplay.vue';
export default {
    props: {
        id: String
    },
    components: { QuestionDisplay },
    data() {
        var question = {
            title: String,
            text: String,
            id: Number,
            position: Number,
            image: String,
            possibleAnswers: Array
        }
        return { question }
    },
    async created() {
        console.log()
        var response = await QuizApiService.getQuestionById(this.id);
        this.question = response.data
    },
    methods: {
        deleteQuestion() {
            let token = AdminStorageService.getToken();
            if (token !== undefined) {
                QuizApiService.delQuestion(token, this.id);
                this.$router.push({ name: "QuestionsList" });
            }
        }
    }

}
</script>