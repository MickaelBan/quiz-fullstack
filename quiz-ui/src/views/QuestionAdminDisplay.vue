<template>
    <div class="cpnt">
        <div class="question">
            <div class="imageQuestion">
                <img v-if="question.image" :src="question.image" />
            </div>
            <div class="titleQuestion">
                <h1>{{ question.title }}</h1>
            </div>
            <div class="textQuestion">
                <h3>{{ question.text }}</h3>
            </div>
            <div class="barAnswers" v-for="(possibleAnswer, index) in question.possibleAnswers">
                <a class="possibleAnswers" v-on:click="$emit('answer-selected', index + 1)">
                    {{ index+ 1}} - {{ possibleAnswer.text }}
                </a>
            </div>
        </div>
    </div>

    <div class="button" id="edit">
        <input type="submit" value="Editer la question">
    </div>
    <div class="button" id="delete">
        <input type="submit" value="Supprimer la question">
    </div>



</template>

<script>
import QuizApiService from '../services/QuizApiService';

export default {
    props: {
        id: String
    },
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