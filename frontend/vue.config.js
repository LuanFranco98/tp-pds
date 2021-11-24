module.exports = {
    // options...
    assetsDir:'static',

    outputDir:'templates',
    
    pages:{
      createPost:{
        entry: 'src/views/post/createPost/createPost.js',
        template: 'public/createPost.html',
        filename: 'createPost.html',
        title:'Create Post'
      },
      createUsuario:{
        entry: 'src/views/usuario/createUsuario/createUsuario.js',
        template: 'public/createUsuario.html',
        filename: 'createUsuario.html',
        title:'Create Usuario'
      },
      postbyCategory:{
        entry: 'src/views/post/postByCategory/postbyCategory.js',
        template: 'public/postbyCategory.html',
        filename: 'postbyCategory.html',
        title:'Post By Category'
      },
      loginUsuario:{
        entry: 'src/views/usuario/loginUsuario/loginUsuario.js',
        template: 'public/loginUsuario.html',
        filename: 'loginUsuario.html',
        title:'Login Usuario'
      },
      postbyUsuario:{
        entry: 'src/views/post/postbyUsuario/postbyUsuario.js',
        template: 'public/postbyUsuario.html',
        filename: 'postbyUsuario.html',
        title:'Post By Usuario'
      },

    }
  }