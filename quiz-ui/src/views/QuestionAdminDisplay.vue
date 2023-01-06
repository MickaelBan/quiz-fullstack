<template>
    <QuestionDisplay :question=question />

    <div class="button" id="edit">
        <input type="submit" value="Editer la question">
    </div>
    <div class="button" id="delete">
        <input type="submit" value="Supprimer la question">
    </div>



</template>

<script>
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
    }
}
</script>