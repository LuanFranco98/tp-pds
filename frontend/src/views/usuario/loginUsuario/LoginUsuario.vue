<template>
    <div id="LoginUsuarioWrapperDiv" style="background-color:#CCC8B3; margin-left:40%; margin-right:40%;margin-top:5%; text-align:center; height:350px; border-radius:15px">
        <br/>
        <h2>Faça aqui seu login</h2>
       
        <div style="margin-left:20%">
            <form v-on:submit.prevent="onSubmit">
                <!-- Header e Email -->
                <div class="form-group row">
                    <span style=" margin-top:2%; font-weight:bold">Digite seu e-mail:</span>
                </div>
                <div class="form-group row">
                    <input  type="text" placeholder="E-mail" v-model="usuario.email" style="width:300px; border-radius:5px;"/>
                </div>
                <!-- Header e Senha -->
                <div class="form-group row">
                    <span style=" font-weight:bold">Digite sua senha:</span>
                </div>
                <div class="form-group row">
                    <input  type="text" placeholder="Senha" v-model="usuario.senha" style="width:300px; border-radius:5px"/>
                </div>
                <!-- Botões -->
                <div class="form-group row">
                    <button class="btn btn-success" style="margin-right:140px;"  v-on:click="submitForm()">Login</button>
                    <button class="btn btn-info "  v-on:click="redirectCreateUsuario()">Cadastrar</button>
                </div>
                
            </form>
        </div>



    </div>
</template>

<script>
    export default {
        name: 'LoginUsuario',

        data(){
            return {
                    usuario:  {},   
                    usuarios: [],                 
                }
        },

        async created(){
            await this.getUsuarios();
        },

        methods:{
            submitForm()
            {
                var arrayLength = this.usuarios.length
                for (let i = 0; i < arrayLength; i++) {                    
                    if(this.usuario.email == this.usuarios[i].email && this.usuario.senha == this.usuarios[i].senha)
                    {
                        //TODO: login
                        console.log("Login");
                        this.usuario =  {};
                        break;
                    }else{
                        //TODO:show login failed mesage
                        console.log("Não existe");
                    }
                }
            },
            redirectCreateUsuario()
            {
                // redirecionar pra pagina de criar usuario
            },
            async getUsuarios(){
                var response = await fetch('http://127.0.0.1:8000/api/usuario/');
                this.usuarios = await response.json();
            }
            
        },
    }
</script>