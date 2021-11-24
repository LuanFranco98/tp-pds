<template>
    <div id="viewPostWrapper">
        <div style="background-color:#CCC8B3; margin-left:15%; margin-right:15%; margin-top:10px;height:500px">
            <div style="margin-left:20px;">
                <h3>Título: {{ post.titulo }}</h3>
                <small>Categorias: {{ post.categorias }}</small>
                <small>Autor:{{ post.criador }}</small>
                <br/>
                <p>{{ post.conteudo }}</p>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'ViewPost',
    data(){
    return {
        post:{}, 
        posts: [],
        //TODO: pegar esse post de forma dinamica, quando o usario clicar no ir para post em alguma das paginas de todos posts, posts da categoria ou posts da pessoa
        postId: 2,
        }
    },
    async created(){
        this.getPost();
    },
    methods:{
        async getPost(){
            var response = await fetch(`http://127.0.0.1:8000/api/post/${this.postId}`);
            this.post = await response.json();
        }
    }
}
</script>
