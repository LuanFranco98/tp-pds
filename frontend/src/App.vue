<template>
  <div id="app">
      <table class="table">
        <thead>
          <th>Nome</th>
          <th>Email</th>
          <th>Senha</th>
        </thead>
        <tbody>
          <tr v-for="usuario in usuarios" :key="usuario.id">
            <td>{{ usuario.nome }}</td>
            <td>{{ usuario.email }}</td>
            <td>{{ usuario.senha }}</td>
          </tr>
        </tbody>
      </table>  

  </div>
</template>

<script>

export default {
  name: 'App',
  data(){
    return {
      usuarios: []
    }
  },
  async created(){
    var response =await fetch('http://127.0.0.1:8000/api/usuario/')
    this.usuarios = await response.json();
  }
}

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
