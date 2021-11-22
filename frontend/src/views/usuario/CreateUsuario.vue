<template>
  <div id="app">
    

  
    <div class="row">
        <div class="col-8 mx-auto mt-5">
          <form v-on:submit.prevent="onSubmit">
            <div class="form-group row">
              <input  type="text" class="form-control col-3 mx-2" placeholder="Nome" v-model="usuario.nome"/>
              <input  type="text" class="form-control col-3 mx-2" placeholder="E-mail" v-model="usuario.email"/>
              <input  type="text" class="form-control col-3 mx-2" placeholder="Senha" v-model="usuario.senha"/>
              <button class="btn btn-success"  v-on:click="submitForm()">{{this.mode}}</button>
            </div>
          </form>

          <table class="table">
            <thead>
              <th>Nome</th>
              <th>Email</th>
              <th>Senha</th>
              <th>Editar usuario</th>
            </thead>
            <tbody>
              <tr v-for="usr in usuarios" :key="usr.id">
                <td>{{ usr.nome }}</td>
                <td>{{ usr.email }}</td>
                <td>{{ usr.senha }}</td>
                <td>
                  <button class="btn btn-success" v-on:click="setUsuario(usr)"> Icone! </button>
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
  name: 'CreateUsuario',
  components: {

  },
  data(){
    return {
      mode: 'Cadastrar',
      usuario:{}, 
      usuarios: []
    }
  },
  async created(){
    this.getUsuarios();
  },

  methods:{
    
    submitForm(){
      if(this.usuario.id == undefined)
      {
        this.mode = 'Cadastrar';
        this.createUsuario();
      }else
      {
        this.editUsuario();
      }
    },

    setUsuario(arg)
    {
      this.mode = 'Editar'
      this.usuario = arg;
    },

    async editUsuario(){ 
      await this.getUsuarios();

      await fetch( `http://127.0.0.1:8000/api/usuario/${this.usuario.id}/` ,
      {
        method: 'put',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.usuario)
      });

      await this.getUsuarios();
      this.usuario = {};
    },

    async getUsuarios(){
      var response = await fetch('http://127.0.0.1:8000/api/usuario/');
      this.usuarios = await response.json();
    },

    async createUsuario(){
      await this.getUsuarios();

      await fetch('http://127.0.0.1:8000/api/usuario/',
      {
        method: 'post',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.usuario)
      });

      await this.getUsuarios();
      this.usuario = {};
    }
  }

}

</script>
<!-- 
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
-->