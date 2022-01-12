<template>
    
    <div id="favoritePosts" style="background-color:#cf5947; margin-left:15%; margin-right:15%; margin-top:10px; display:grid ; border-radius: 10px ">        
        <div v-for="postagem in this.posts" :key="postagem.id"  style="background-color: #D75A3E; margin-left:5%; margin-right:5%; margin-bottom:1%; margin-top:1%  ; border-radius: 10px; display:grid ;border-style: solid;">
            <div style="margin:2%; background-color: #D75A3E;">
                <h3>{{ postagem.titulo }}</h3>
                <p>{{ postagem.conteudo.slice(0, 200) + ' ... '  }}</p>
                <br/>
                <button class="btn btn-info" style="margin-left:20px" >Seguir Post</button>
            </div>
        </div> 
    </div>
</template>

<script>
    export default {
        name: 'FavoritePosts',

        data(){
        return {
            favoritos: [],
            posts: {}
            }
        },
        
        async created(){
            this.getFavoritos();
        },

        methods:
        {
            async getFavoritos()
            {
                var response = await fetch('http://127.0.0.1:8000/api/usuario/22');
                response = await response.json();
                this.favoritos = response.favoritos
                this.getPostagens()
            },

            async getPostagens()
            {     
                var arrayLength = this.favoritos.length;
                this.posts = [];

                for (let i = 0; i < arrayLength; i++) {
                    var response = await fetch(`http://127.0.0.1:8000/api/post/${this.favoritos[i]}`);
                    var temp_post = await response.json();

                    this.posts.push(temp_post);
                }               
                
            },
            

            
        }

    }
</script>