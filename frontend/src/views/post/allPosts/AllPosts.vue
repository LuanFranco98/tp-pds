<template>
    <div id="PostByCategory" style="background-color:#cf5947; margin-left:15%; margin-right:15%; margin-top:10px; display:grid ; border-radius: 10px ">
        <div v-for="postagem in this.posts" :key="postagem.id"  style="background-color: #D75A3E; margin-left:5%; margin-right:5%; margin-bottom:1% ; margin-top:1% ; border-radius: 10px; display:grid ;border-style: solid;">
                <div style="margin-left:20px;margin-right:10px">
                    <h3><strong>{{ postagem.titulo }}</strong></h3>
                    <!-- <small>Categorias: {{ postagem.categorias }}</small>
                    <small>Autor:{{ postagem.criador }}</small>
                    <br/> -->
                    <p>{{ postagem.conteudo.slice(0, 200) + ' ... ' }}</p>
                    
                    <button class="btn btn-info" style="margin-left:5px; margin-bottom:10px" ><a href="#" style="text-decoration:inherit ;color: inherit;background-color: inherit;">Continuar lendo</a></button>
                </div>
            </div>
    </div>
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
