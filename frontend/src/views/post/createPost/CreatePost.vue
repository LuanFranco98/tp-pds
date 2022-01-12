<template>
    <div id="CreatePostDiv" style="background-color:#cf5947; margin-left:15%; margin-right:15%; margin-top:10px; display:grid ; border-radius: 10px ">
      <div class="row" >
        <div class="col-8 mx-auto mt-5">
          <h3>Cadastrar novo post</h3>
          <form v-on:submit.prevent="onSubmit">
                <p style="font-weight:bold">Digite aqui o título do seu post:</p>
                <input  type="text"  placeholder="Título" v-model="post.nome"/>
                <br/>
                <br/>
                <p style="font-weight:bold">Digite aqui as categorias do seu post:</p>
                <select @change="setCategoria($event)" class="form-select form-control" style="width:350px;" multiple>
                    <option> --- Selecione as categorias do seu post --- </option>
                    <option v-for="categoria in this.categorias" :key="categoria.id" :value="categoria.id"> {{ categoria.nome }} </option>
                </select>
                <br/>
                <br/>
                <p style="font-weight:bold">Digite aqui o conteúdo do seu post:</p>
                <textarea  placeholder="Conteúdo" v-model="post.conteudo" style="width:700px; height:400px" />
                <br/>
                <br/>
                <p style="font-weight:bold">Digite aqui o link para a sua imagem:</p>
                <input  type="text"  placeholder="Link da imagem" v-model="post.imagem"/>
                <br/>
                <button class="btn btn-success" style="margin-top:10px; width:200px; height:50px" >Criar novo Post</button>
              
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
        usuario:{}, 
        post:{}, 
        categorias: {},
        }
    },
    async created(){
        this.getCategorias();
        //TODO: adicionar usuario criador no this.post
        var response = await fetch('http://127.0.0.1:8000/api/usuario/22');
        this.post.criador = await response.json();
    },
    methods:{
        submitForm(){
            this.createPost();
        },
        async createPost(){
            await fetch('http://127.0.0.1:8000/api/post/',
            {
              method: 'post',
              headers: {
                'Content-Type': 'application/json'
              },
              body: JSON.stringify(this.post)
            });

        },
        async getCategorias()
        {
            var response = await fetch('http://127.0.0.1:8000/api/categoria');
            this.categorias = await response.json();
        },
        setCategoria(e)
        {
            this.post.categorias = [];
            this.post.categorias.push(e.target.value);
        },

    }
}

</script>