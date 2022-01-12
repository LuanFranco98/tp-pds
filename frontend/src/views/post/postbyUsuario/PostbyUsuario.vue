<template>
    <div id="posbyUsuarioWrapper" style="background-color:#cf5947; margin-left:15%; margin-right:15%; margin-top:10px; display:grid ; border-radius: 10px ">
        <div v-for="postagem in userRelatedPosts" :key="postagem.id"  style="background-color: #D75A3E; margin-left:5%; margin-right:5%; margin-bottom:1% ; margin-top:1% ; border-radius: 10px; display:grid ;border-style: solid;">
            <div style="margin-left:20px;margin-right:10px">
                <h3><strong>{{ postagem.titulo }}</strong></h3>
                <!-- <small>Categorias: {{ postagem.categorias }}</small>
                <small>Autor:{{ postagem.criador }}</small>
                <br/> -->
                <p>{{ postagem.conteudo.slice(0, 200) + ' ... ' }}</p>
                    
                <button class="btn btn-info" style="margin-left:5px; margin-bottom:10px;"><a href="#" style="text-decoration:inherit ;color: inherit;background-color: inherit;">Continuar lendo</a> </button>
            </div>
        </div>
    </div>
</template>

<script>
export default {
        name: 'PostbyUsuario',

        data(){
        return {
            usuarioId: 22,
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
                        this.userRelatedPosts.push(this.posts[i]);
                    }
                }       
                //como pode isso aqui ser size 15 se la em cima é  e ele so entra no if 1 vez?
                console.log("size do userRelatedPosts:  "+ this.userRelatedPosts.length)        
            }
        }
}
</script>