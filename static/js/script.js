let selec = document.querySelector(".add__type");
const formElement = document.querySelector(".add__container");
const newForm = `
    <div class="add__container">
      <select class="add__type">
        <option value="iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii" selected>+</option>
        <option value="eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee">-</option>
      </select>
      
      <input
        type="text"
        class="add__description"
        placeholder="Add description"
      />
      <input type="number" class="add__value" name="desc" placeholder="Value" />
    </div>
`;
selec.addEventListener("change", val => {

    formElement.insertAdjacentHTML("beforeend", newForm)
});

console.log("Start here");