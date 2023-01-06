<template>

    <div class="button" id="edit">Editer la question</div>
    <div class="button" id="delete">Supprimer la question</div>

    <div class="question">
        <!-- <a>{{ question.title }}</a> -->
    </div>

</template>

<script>

export default {
    name: "QuestionAdminDisplay", 
    props: ['question'],
    mounted(){
        console.log(this.question);
    },
    methods: {
        handler(question){
            console.log(question);
        }
    }
}
</script>