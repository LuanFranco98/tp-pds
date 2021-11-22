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
                <p style="font-weight:bold">Digite aqui o conteúdo do seu post</p>
                <textarea  placeholder="Conteúdo" v-model="post.conteudo" style="width:700px; height:400px" />
                <br/>
                <br/>
                <p style="font-weight:bold">Digite aqui a categoria do seu post</p>
                <input  type="text"  placeholder="Categoria" v-model="post.categoria"/> <!-- mudar pra um selectonemenu -->
                <br/>
                <br/>
                <!-- uploadFile v-model="post.imagem"-->
                <button class="btn btn-success" style="margin-left:20px" >Cadastrar</button>
              
            </form>
          <br/>
          <br/>
          <table class="table">
          <thead>
            <th>Titulo</th>
            <th>Conteudo</th>
            <th>Imagem</th>
            <th>Criador</th>
            <th>Categoria</th>
            <th>Botão</th>
          </thead>
          <tbody>
            <tr v-for="postagem in posts" :key="postagem.id">
              <td>{{ postagem.titulo }}</td>
              <td>{{ postagem.conteudo }}</td>
              <td>{{ postagem.imagem }}</td>
              <td>{{ postagem.criador }}</td>
              <td>{{ postagem.categoria }}</td>
              <td>
                <button class="btn btn-success" > Icone! </button>
              </td>
            </tr>
          </tbody>
        </table>  
      </div>
    </div>
  </div>
</template>

<script>
    export default {
    name: 'CreatePost',
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