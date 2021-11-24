<template>
    <table class="table" >
        <div v-for="postagem in this.posts" :key="postagem.id"  style="background-color:#CCC8B3; margin-left:15%; margin-right:15%; margin-top:10px;">
                <div style="margin-left:20px;">
                    <h3>Título: {{ postagem.titulo }}</h3>
                    <small>Categorias: {{ postagem.categorias }}</small>
                    <small>Autor:{{ postagem.criador }}</small>
                    <br/>
                    <p>{{ postagem.conteudo }}</p>
                    
                    <button class="btn btn-info" style="margin-left:5px; margin-bottom:10px" >Seguir Post</button>
                </div>
            </div>
    </table>  
</template>

<script>
export default {
    name: 'AllPosts',
    data(){
    return {
        post:{}, 
        posts: []
        }
    },
    async created(){
        this.getPosts();
    },
    methods:{
        async getPosts(){
            var response = await fetch('http://127.0.0.1:8000/api/post/');
            this.posts = await response.json();
        }
    }
}
</script>
