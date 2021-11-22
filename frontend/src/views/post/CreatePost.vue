<template>
    <div id="CreatePostDiv">
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
          <tr v-for="usr in posts" :key="usr.id">
            <td>{{ usr.titulo }}</td>
            <td>{{ usr.conteudo }}</td>
            <td>{{ usr.imagem }}</td>
            <td>{{ usr.criador.nome }}</td>
            <td>{{ usr.categoria.nome }}</td>
            <td>
              <button class="btn btn-success" > Icone? </button>
            </td>
          </tr>
        </tbody>
      </table>  
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