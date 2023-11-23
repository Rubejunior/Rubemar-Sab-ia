<script>
        function avancarParaPasso(passo) {
            document.querySelectorAll('.passo').forEach(function(el) {
                el.style.display = 'none';
            });
            document.querySelector('#passo' + passo).style.display = 'block';
        }

        // Iniciando com o Passo 1
        avancarParaPasso(1);
    </script>