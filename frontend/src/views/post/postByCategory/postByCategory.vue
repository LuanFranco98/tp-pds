<template>
    
    <div>
        <select @change="setCategoria($event)" class="form-select form-control">
            <option> --- Selecione uma categoria --- </option>
            <option v-for="categoria in categorias" :key="categoria.id" :value="categoria.id"> {{ categoria.nome }} </option>
        </select>
        <div v-if="categoriaSelecionada != null">
            <div v-for="postagem in posts" :key="postagem.id"  style="background-color:#CCC8B3; margin-left:15%; margin-right:15%">
                <h3>Título: {{ postagem.titulo }}</h3>
                <small>Categorias: {{ postagem.categorias }}</small>
                <small>Autor:{{ postagem.criador }}</small>
                <br/>
                <p>{{ postagem.conteudo }}</p>
                <button class="btn btn-info" style="margin-left:20px" >Seguir Post</button>
            </div>
        </div>
        
    </div>
</template>

<script>
    export default {
        name: 'PostByCategory',
        data(){
        return {
            categoriaSelecionada: null,
            categorias: {},
            post:{}, 
            posts: []
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
            }
            
        }

    }
</script>