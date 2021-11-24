<template>
    <div id="posbyUsuarioWrapper">
        <div v-for="postagem in userRelatedPosts" :key="postagem.id"  style="background-color:#CCC8B3; margin-left:15%; margin-right:15%; margin-top:10px; border-radius:5px">
            <h3>Título: {{ postagem.titulo }}</h3>
            <small>Categorias: {{ postagem.categorias }}</small>
            <small>Autor:{{ postagem.criador }}</small>
            <br/>
            <p>{{ postagem.conteudo }}</p>
            <br/>
            <button class="btn btn-info" style="margin-left:20px" >Seguir Post</button>
        </div>
    </div>
</template>

<script>
export default {
        name: 'PostbyUsuario',

        data(){
        return {
            usuarioId: 18,
            post:{}, 
            posts: {},
            userRelatedPosts: [],
            }
        },
        
        async created(){
            await this.getPosts();
            await this.getUserRelatedPosts();
        },

        methods: {
            async getPosts(){
                var response2 = await fetch('http://127.0.0.1:8000/api/post/');
                this.posts = await response2.json();
            },

            async getUserRelatedPosts(){
                var arrayLength = this.posts.length;
                this.userRelatedPosts = [];
                //size 0
                console.log("size do userRelatedPosts:  "+ this.userRelatedPosts.length) 
                console.log("size do posts:  "+ this.posts.length)   
                for (let i = 0; i < arrayLength; i++) {
                    if( this.posts[i].criador == this.usuarioId )
                    {
                        //entra aqui so  uma vez
                        console.log("entrou no if")
                        console.log("post: " + this.posts[i]);
                        console.log("post title: " + this.posts[i].titulo)
                        this.userRelatedPosts += this.posts[i];
                    }
                }       
                //como pode isso aqui ser size 15 se la em cima é  e ele so entra no if 1 vez?
                console.log("size do userRelatedPosts:  "+ this.userRelatedPosts.length)        
            }
        }
}
</script>