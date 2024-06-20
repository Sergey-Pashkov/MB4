function toggleEditMode(constantId) {
    const isChecked = document.getElementById('edit_mode_' + constantId).checked;
    const valueField = document.getElementById('value_' + constantId);
    const commentField = document.getElementById('comment_' + constantId);

    if (isChecked) {
        valueField.removeAttribute('readonly');
        commentField.removeAttribute('readonly');
    } else {
        valueField.setAttribute('readonly', 'readonly');
        commentField.setAttribute('readonly', 'readonly');
    }
}

document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.form-check-input').forEach(function(checkbox) {
        checkbox.addEventListener('change', function() {
            const constantId = this.id.split('_')[2];
            toggleEditMode(constantId);
        });
    });
});
