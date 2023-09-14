 $(document).ready(function() {
           $('#select_issue').change(function() {
               var selection = $(this).val();

               $.ajax({
                   type: 'POST',
                   url: '/get_records',
                   data: {selection:selection},
                   success: function(response) {
                       var recordsSelect = $('#records');
                       recordsSelect.empty();

<!--alert(JSON.stringify(response));-->
                       for (var i = 0; i < response.length; i++) {
                            var platformId = response[i].platform_id;
                            var platformName = response[i].platform_name;

                            recordsSelect.append($('<option>', {
                            value: platformId,
                            text: platformName
                             }));
                        }
                    },
                   error: function(error) {
                       console.log(error);
                   }
               });
           });
       });

