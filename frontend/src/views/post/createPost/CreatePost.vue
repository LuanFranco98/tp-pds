<template>
    <div id="CreatePostDiv" style="background-color:#CCC8B3; margin-left:15%; margin-right:15%">
      <div class="row">
        <div class="col-8 mx-auto mt-5">
          <h3>Cadastrar novo post</h3>
          <form v-on:submit.prevent="onSubmit">
                <p style="font-weight:bold">Digite aqui o título do seu post</p>
                <input  type="text"  placeholder="Título" v-model="post.nome"/>
                <br/>
                <br/>
                <p style="font-weight:bold">Digite aqui as categorias do seu post</p>
                <select @change="setCategoria($event)" class="form-select form-control" style="width:250px;" multiple>
                    <option> --- Selecione as categorias do seu post --- </option>
                    <option v-for="categoria in this.categorias" :key="categoria.id" :value="categoria.id"> {{ categoria.nome }} </option>
                </select>
                <br/>
                <br/>
                <p style="font-weight:bold">Digite aqui o conteúdo do seu post</p>
                <textarea  placeholder="Conteúdo" v-model="post.conteudo" style="width:700px; height:400px" />
                <br/>
                <br/>
                <p style="font-weight:bold">Digite aqui o link para a sua imagem</p>
                <input  type="text"  placeholder="Link da imagem" v-model="post.imagem"/>
 
                <button class="btn btn-success" style="margin-left:5px; width:200px; height:50px" >Criar novo Post</button>
              
            </form>
          <br/>
          <br/>
          
      </div>
    </div>
  </div>
</template>

<script>
    export default {
    name: 'CreatePost',
    data(){
    return {
        mode: 'Cadastrar',
        post:{}, 
        posts: [],
        categorias: {},
        }
    },
    async created(){
        this.getCategorias();
    },
    methods:{
        submitForm(){
            this.createPost();
        },
        async createPost(){
            //adicionar usuario criador no this.post
            await fetch('http://127.0.0.1:8000/api/post/',
            {
              method: 'post',
              headers: {
                'Content-Type': 'application/json'
              },
              body: JSON.stringify(this.post)
            });

            this.usuario = {};
        },
        async getCategorias()
        {
            var response = await fetch('http://127.0.0.1:8000/api/categoria');
            this.categorias = await response.json();
        },
        setCategoria(e)
        {
            this.getPostagens(e.target.value)
            this.categoriaSelecionada = e.target.value ;
        },

    }

}

</script>