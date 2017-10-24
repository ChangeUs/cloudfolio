(function($) {

  'use strict';
  $('#btnTabCreation').click(function() {
      var size = $('input[name=slideup_toggler]:checked').val()
      var modalElem = $('#modalSlideUp');
      $('#modalTapCreation').modal('show');
      modalElem.children('.modal-dialog').removeClass('modal-lg')
  });

})(window.jQuery);
