<?php
require('php_scripts/load_options.php');
$lo = new LoadOptions();
$languages = $lo->get_languages();
$encodings = $lo->get_encodings();
?>
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Syllabification</title>
    <link href="style/style.css" rel="stylesheet" media="all">
</head>

<script>
    function validateForm() {
        var file_name = document.forms["myform"]["file"].value;
        if (file_name === "") {
            alert("Please, choose the file.");
            return false;
        }
        var extension = file_name.split('.').pop();
        if ( extension !== "txt") {
            alert("Only txt extention is allowed.");
            return false;
        }
    }
</script>

<body>

<div class="content">

    <h1>Analysis of linguistic data &mdash; Syllabification</h1>

    <nav>
        <a href="index.php" class="chosen">Select a file </a>
        <a href="text_index.php">Insert the text </a>
    </nav>

    <div class="form">

        <input type="hidden" name="type" value="file" form="myform">

        <div class="inputFile">
            <input type="file" name="file" form="myform">
            <p class="hint">Extension: txt</p>
        </div>

        <div class="properties">

            <div class="encoding">
                <label for="encoding">Encoding</label>
                <select name="encoding" form="myform">
                    <?php
                    foreach ($encodings as $option => $value)
                        echo "<option value='$value'>$option</option>";
                    ?>
                </select>
            </div>

            <div class="language">
                <label for="language">Language</label>
                <select name="language" form="myform">
                    <?php
                    foreach ($languages as $option => $value)
                        echo "<option value='$value'>$option</option>";
                    ?>
                </select>
            </div>

        </div>

        <div class="submit">
            <input type="submit" name="submit" value="Submit" form="myform">
        </div>

        <form id="myform" action="php_scripts/upload.php" method="post" enctype="multipart/form-data" onsubmit="return validateForm()"></form>

    </div>

    <footer>
        <p>&copy; 2019 Hallaballoo</p>
    </footer>

</div>

</body>
</html>
