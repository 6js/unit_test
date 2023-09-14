$(document).ready(function() {
    // Prevent default behavior when files are dragged and dropped
    $(document).on('dragover', function(e) {
        e.preventDefault();
    });

    // Handle the file drop event
    $(document).on('drop', '#drop-area', function(e) {
        e.preventDefault();
        var files = e.originalEvent.dataTransfer.files;
        handleFiles(files);
    });

    // Handle the file selection event (input type="file")
    $(document).on('change', '#file-input', function(e) {
        var files = e.target.files;
        handleFiles(files);
    });

    // Handle the click event for the upload button
    $(document).on('click', '#upload-button', function(e) {
        var files = $('#file-input')[0].files;
        handleFiles(files);
    });

    // Update the table when the page loads
    updateTable();

    // Function to handle file upload and display
    function handleFiles(files) {
        var fileList = $('#file-list ul');
        fileList.empty();

        for (var i = 0; i < files.length; i++) {
            var file = files[i];
            var listItem = $('<li>').text(file.name);
            fileList.append(listItem);
        }

        // AJAX upload to Flask backend
        var formData = new FormData();
        for (var i = 0; i < files.length; i++) {
            formData.append('file', files[i]);
        }

        $.ajax({
            type: 'POST',
            url: '/upload',
            data: formData,
            processData: false,
            contentType: false,
            success: function(data) {
                console.log(data); // You can handle the server response here if needed
                updateTable(); // Refresh the table dynamically after upload
            },
            error: function(error) {
                console.error(error);
            }
        });
    }

    // Function to update the table dynamically after upload
    function updateTable() {
        $.ajax({
            type: 'GET',
            url: '/get_files',
            dataType: 'json',
            success: function(data) {
                var newTableBody = '';
                for (var i = 0; i < data.length; i++) {
                    newTableBody += '<tr>';
                    newTableBody += '<td>' + data[i].id + '</td>';
                    newTableBody += '<td>' + data[i].filename + '</td>';
                    newTableBody += '<td>' + data[i].file_path + '</td>';
                    newTableBody += '</tr>';
                }
                $('#file-table-body').html(newTableBody);
            },
            error: function(error) {
                console.error(error);
            }
        });
    }
});
