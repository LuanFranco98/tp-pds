<template>
    
    <div id="PostByCategory" style="background-color:#CCC8B3; margin-left:15%; margin-right:15%">
        <select @change="setCategoria($event)" class="form-select form-control" style="width:250px;  margin-left:10%;">
            <option> --- Selecione uma categoria --- </option>
            <option v-for="categoria in this.categorias" :key="categoria.id" :value="categoria.id"> {{ categoria.nome }} </option>
        </select>
        <br/>
        <div v-if="categoriaSelecionada != null">
            <div v-for="postagem in this.posts" :key="postagem.id"  style="background-color:#CCC8B3; margin-left:15%; margin-right:15%">
                <h3>Título: {{ postagem.titulo }}</h3>
                <small>Categorias: {{ postagem.categorias }}</small>
                <small>Autor:{{ postagem.criador }}</small>
                <br/>
                <p>{{ postagem.conteudo }}</p>
                <br/>
                <button class="btn btn-info" style="margin-left:20px" >Seguir Post</button>
            </div>
        </div>
        
    </div>
</template>

<script>
    export default {
        name: 'PostbyCategory',

        data(){
        return {
            categoriaAnterior:null,
            categoriaSelecionada: null,
            categorias: {},
            post:{}, 
            posts: {}
            }
        },
        
        async created(){
            this.getCategorias();
        },

        methods:
        {
            async getCategorias()
            {
                var response = await fetch('http://127.0.0.1:8000/api/categoria');
                this.categorias = await response.json();
            },
            setCategoria(e)
            {
                this.categoriaSelecionada = e.target.value ;
                this.getPostagens(e.target.value)
            },
            async getPostagens(selecionado)
            {                    
                var response = await fetch(`http://127.0.0.1:8000/api/categoria/${selecionado}`);
                var categoria = await response.json();
                console.log("posts.size(): "+ categoria.posts.length);
                var arrayLength = categoria.posts.length;
                this.posts = [];

                for (let i = 0; i < arrayLength; i++) {
                    console.log("element: " +categoria.posts[i]);
                    var response2 = await fetch(`http://127.0.0.1:8000/api/post/${categoria.posts[i]}`);
                    var temp_post = await response2.json();
                    console.log("post: "+ temp_post);
                    console.log("post title: " +temp_post.titulo)
                    this.posts.push(temp_post);
                }               
                
            },
            

            
        }

    }
</script>