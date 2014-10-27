/**
 * Created by Barbara on 26/10/2014.
 */


$(document).ready(function () {

    var $clienteForm = $('#cliente-form');
    $clienteForm.hide();
    $('#mostrar-form-btn').click(function () {
        $clienteForm.slideToggle();
    });

    var $cpfInput = $('#cpfInput');
    var $nomeInput = $('#nomeInput');
    var $rgInput = $('#rgInput');
    var $nascimentoInput = $('#nascimentoInput');
    var $nacionalidadeInput = $('#nacionalidadeInput');
    var $estado_civilInput = $('#estado_civilInput');
    var $profissaoInput = $('#profissaoInput');
    var $complementoInput = $('#complementoInput');
    var $cepInput = $('#cepInput');
    var $enderecoInput = $('#enderecoInput');
    var $numeroInput = $('#numeroInput');
    var $bairroInput = $('#bairroInput');
    var $cidadeInput = $('#cidadeInput');
    var $estadoInput = $('#estadoInput');
    var $telefoneInput = $('#telefoneInput');
    var $celularInput = $('#celularInput');
    var $emailInput = $('#emailInput');

    var $ajaxGif = $('#ajax-gif');

    var $cpfDiv = $('#cpfDiv');
    var $nomeDiv = $('#nomeDiv');
    var $rgDiv = $('#rgDiv');
    var $nascimentoDiv = $('#nascimentoDiv');
    var $nacionalidadeDiv = $('#nacionalidadeDiv');
    var $estado_civilDiv = $('#estado_civilDiv');
    var $profissaoDiv = $('#profissaoDiv');
    var $cepDiv = $('#cepDiv');
    var $enderecoDiv = $('#enderecoDiv');
    var $numeroDiv = $('#numeroDiv');
    var $bairroDiv = $('#bairroDiv');
    var $cidadeDiv = $('#cidadeDiv');
    var $estadoDiv = $('#estadoDiv');
    var $telefoneDiv = $('#telefoneDiv');
    var $celularDiv = $('#celularDiv');
    var $emailDiv = $('#emailDiv');

    $ajaxGif.hide();
    var $salvarBtn = $('#salvar-btn');

    var $helpCpfSpan = $('#help-cpf');
    var $helpNomeSpan = $('#help-nome');
    var $helpRgSpan = $('#help-rg');
    var $helpNascimentoSpan = $('#help-nascimento');
    var $helpNacionalidadeSpan = $('#help-nacionalidade');
    var $helpEstado_CivilSpan = $('#help-estado_civil');
    var $helpProfissaoSpan = $('#help-profissao');
    var $helpCepSpan = $('#help-cep');
    var $helpEnderecoSpan = $('#help-endereco');
    var $helpNumeroSpan = $('#help-numero');
    var $helpBairroSpan = $('#help-bairro');
    var $helpCidadeSpan = $('#help-cidade');
    var $helpEstadoSpan = $('#help-estado');
    var $helpTelefoneSpan = $('#help-telefone');
    var $helpCelularSpan = $('#help-celular');
    var $helpEmailSpan = $('#help-email');

    var $corpoTabela = $('#corpo-tabela');

    var adicionarLinha=function adicionarLinha(cliente) {
        var linha = '<tr id="tr' + cliente.id + '"> ' +
            '<td></td>' +
            '<td>' + cliente.id + '</td>' +
            '<td>' + cliente.cpf + '</td>' +
            '<td>' + cliente.nome + '</td>' +
            '<td>' + cliente.rg + '</td>' +
            '<td>' + cliente.telefone + '</td>' +
            '<td>' + cliente.celular + '</td>' +
            '<td>' + cliente.email + '</td>' +
            '<td><button id="bt' + cliente.id + '" class="btn btn-success btn-sm"><i class="glyphicon glyphicon-plus"></i>Detalhes</button>' +
            '</td> </tr>';

        $corpoTabela.prepend(linha);

        var $linhaHtml = $('#tr' + cliente.id);

        $linhaHtml.hide();
        $linhaHtml.fadeIn();



    }

    $.get('/clientes/rest').success(function (listaDeClientes) {
        for (var i = 0; i < listaDeClientes.length; i += 1) {
            adicionarLinha(listaDeClientes[i]);
        }
    });

    $salvarBtn.click(function () {
        var cliente = {cpf: $cpfInput.val(),
                       nome: $nomeInput.val(),
                       rg: $rgInput.val(),
                       nascimento: $nascimentoInput.val(),
                       nacionalidade: $nacionalidadeInput.val(),
                       estado_civil: $estado_civilInput.val(),
                       profissao: $profissaoInput.val(),
                       complemento: $complementoInput.val(),
                       cep: $cepInput.val(),
                       endereco: $enderecoInput.val(),
                       numero: $numeroInput.val(),
                       bairro: $bairroInput.val(),
                       cidade: $cidadeInput.val(),
                       estado: $estadoInput.val(),
                       telefone: $telefoneInput.val(),
                       celular: $celularInput.val(),
                       email: $emailInput.val()};

        $ajaxGif.slideDown();
        $salvarBtn.hide();

        var cliente_psalvar = $.post('/clientes/rest/save', cliente);
        cliente_psalvar.success(function (cliente_do_servidor) {
            $cpfInput.val("");
            $cpfDiv.removeClass('has-error');
            $helpCpfSpan.text("");

            $nomeInput.val("");
            $nomeDiv.removeClass('has-error');
            $helpNomeSpan.text("");

            $rgInput.val("");
            $rgDiv.removeClass('has-error');
            $helpRgSpan.text("");

            $nascimentoInput.val("");
            $nascimentoDiv.removeClass('has-error');
            $helpNascimentoSpan.text("");

            $nacionalidadeInput.val("");
            $nacionalidadeDiv.removeClass('has-error');
            $helpNacionalidadeSpan.text("");

            $estado_civilInput.val("");
            $estado_civilDiv.removeClass('has-error');
            $helpEstado_CivilSpan.text("");

            $profissaoInput.val("");
            $profissaoDiv.removeClass('has-error');
            $helpProfissaoSpan.text("");

            $complementoInput.val("");

            $cepInput.val("");
            $cepDiv.removeClass('has-error');
            $helpCepSpan.text("");

            $enderecoInput.val("");
            $enderecoDiv.removeClass('has-error');
            $helpEnderecoSpan.text("");

            $numeroInput.val("");
            $numeroDiv.removeClass('has-error');
            $helpNumeroSpan.text("");

            $bairroInput.val("");
            $bairroDiv.removeClass('has-error');
            $helpBairroSpan.text("");

            $cidadeInput.val("");
            $cidadeDiv.removeClass('has-error');
            $helpCidadeSpan.text("");

            $estadoInput.val("");
            $estadoDiv.removeClass('has-error');
            $helpEstadoSpan.text("");

            $telefoneInput.val("");
            $telefoneDiv.removeClass('has-error');
            $helpTelefoneSpan.text("");

            $celularInput.val("");
            $celularDiv.removeClass('has-error');
            $helpCelularSpan.text("");

            $emailInput.val("");
            $emailDiv.removeClass('has-error');
            $helpEmailSpan.text("");

            $clienteForm.fadeOut();
            adicionarLinha(cliente_do_servidor);
        });


        cliente_psalvar.error(function (errors) {

            if (errors.responseJSON != null && errors.responseJSON.cpf != null) {
                $cpfDiv.addClass('has-error');
                $helpCpfSpan.text(errors.responseJSON.cpf);
            } else {
                $cpfDiv.removeClass('has-error');
                $helpCpfSpan.text("");
             }

             if (errors.responseJSON != null && errors.responseJSON.nome != null) {
                 $nomeDiv.addClass('has-error');
                 $helpNomeSpan.text(errors.responseJSON.nome);
             } else {
                $nomeDiv.removeClass('has-error');
                $helpNomeSpan.text("");
             }

             if (errors.responseJSON != null && errors.responseJSON.rg != null) {
                 $rgDiv.addClass('has-error');
                 $helpRgSpan.text(errors.responseJSON.rg);
             } else {
                $rgDiv.removeClass('has-error');
                $helpRgSpan.text("");
             }

             if (errors.responseJSON != null && errors.responseJSON.nascimento != null) {
                 $nascimentoDiv.addClass('has-error');
                 $helpNascimentoSpan.text(errors.responseJSON.nascimento);
             } else {
                $nascimentoDiv.removeClass('has-error');
                $helpNascimentoSpan.text("");
             }

             if (errors.responseJSON != null && errors.responseJSON.nacionalidade != null) {
                 $nacionalidadeDiv.addClass('has-error');
                 $helpNacionalidadeSpan.text(errors.responseJSON.nacionalidade);
             } else {
                $nacionalidadeDiv.removeClass('has-error');
                $helpNacionalidadeSpan.text("");
             }

             if (errors.responseJSON != null && errors.responseJSON.estado_civil != null) {
                 $estado_civilDiv.addClass('has-error');
                 $helpEstado_CivilSpan.text(errors.responseJSON.estado_civil);
             } else {
                $estado_civilDiv.removeClass('has-error');
                $helpEstado_CivilSpan.text("");
             }

             if (errors.responseJSON != null && errors.responseJSON.profissao != null) {
                 $profissaoDiv.addClass('has-error');
                 $helpProfissaoSpan.text(errors.responseJSON.profissao);
             } else {
                $profissaoDiv.removeClass('has-error');
                $helpProfissaoSpan.text("");
             }

             if (errors.responseJSON != null && errors.responseJSON.cep != null) {
                 $cepDiv.addClass('has-error');
                 $helpCepSpan.text(errors.responseJSON.cep);
             } else {
                $cepDiv.removeClass('has-error');
                $helpCepSpan.text("");
             }

             if (errors.responseJSON != null && errors.responseJSON.endereco != null) {
                 $enderecoDiv.addClass('has-error');
                 $helpEnderecoSpan.text(errors.responseJSON.endereco);
             } else {
                $enderecoDiv.removeClass('has-error');
                $helpEnderecoSpan.text("");
             }

             if (errors.responseJSON != null && errors.responseJSON.numero != null) {
                 $numeroDiv.addClass('has-error');
                 $helpNumeroSpan.text(errors.responseJSON.numero);
             } else {
                $numeroDiv.removeClass('has-error');
                $helpNumeroSpan.text("");
             }

             if (errors.responseJSON != null && errors.responseJSON.bairro != null) {
                 $bairroDiv.addClass('has-error');
                 $helpBairroSpan.text(errors.responseJSON.bairro);
             } else {
                $bairroDiv.removeClass('has-error');
                $helpBairroSpan.text("");
             }

             if (errors.responseJSON != null && errors.responseJSON.cidade != null) {
                 $cidadeDiv.addClass('has-error');
                 $helpCidadeSpan.text(errors.responseJSON.cidade);
             } else {
                $cidadeDiv.removeClass('has-error');
                $helpCidadeSpan.text("");
             }

             if (errors.responseJSON != null && errors.responseJSON.estado != null) {
                 $estadoDiv.addClass('has-error');
                 $helpEstadoSpan.text(errors.responseJSON.estado);
             } else {
                $estadoDiv.removeClass('has-error');
                $helpEstadoSpan.text("");
             }

             if (errors.responseJSON != null && errors.responseJSON.telefone != null) {
                 $telefoneDiv.addClass('has-error');
                 $helpTelefoneSpan.text(errors.responseJSON.telefone);
             } else {
                $telefoneDiv.removeClass('has-error');
                $helpTelefoneSpan.text("");
             }

             if (errors.responseJSON != null && errors.responseJSON.celular != null) {
                 $celularDiv.addClass('has-error');
                 $helpCelularSpan.text(errors.responseJSON.celular);
             } else {
                 $celularDiv.removeClass('has-error');
                 $helpCelularSpan.text("");
             }

             if (errors.responseJSON != null && errors.responseJSON.email != null) {
                 $emailDiv.addClass('has-error');
                 $helpEmailSpan.text(errors.responseJSON.email);
             } else {
                 $emailDiv.removeClass('has-error');
                 $helpEmailSpan.text("");
             }
        });

        cliente_psalvar.always(function () {
            $ajaxGif.slideUp();
            $salvarBtn.slideDown();
        })
    });

});