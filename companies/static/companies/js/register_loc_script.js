const companyType = document.getElementById("id_company_type");
const companyName = document.getElementById("id_company_name");
const posPerAcc = document.getElementById("id_pos_per_acc");
const positionNom = document.getElementById("id_position_nom");
const actingOn = document.getElementById("id_acting_on");
const legalAddr = document.getElementById("id_legal_addr");
const postalAddr = document.getElementById("id_postal_addr");
const registrationAddr = document.getElementById("id_registration_addr");
const kpp = document.getElementById("id_kpp");
const ogrn = document.getElementById("id_ogrn");
const okpo = document.getElementById("id_okpo");
const passportSeries = document.getElementById("id_passport_series");
const passportNumber = document.getElementById("id_passport_number");
const passIssuedBy = document.getElementById("id_pass_issued_by");
const passIssuedDate = document.getElementById("id_pass_issued_date");
const passIssuedCode = document.getElementById("id_pass_issued_code");


companyType.addEventListener("keyup", (e) => {
  const value = e.currentTarget.value;


  if (value === "ООО") {
    companyName.value = "";
    registrationAddr.value = "НЕ ЗАПОЛНЯЕТСЯ";
    posPerAcc.value = "";
    positionNom.value = "";
    actingOn.value = "";
    legalAddr.value = "";
    postalAddr.readonly = "";
    kpp.value = "";
    ogrn.value = "";
    okpo.value = "";
    passportSeries.value = "НЕ ЗАПОЛНЯЕТСЯ";
    passportNumber.value = "НЕ ЗАПОЛНЯЕТСЯ";
    passIssuedBy.value = "НЕ ЗАПОЛНЯЕТСЯ";
    passIssuedDate.value = "НЕ ЗАПОЛНЯЕТСЯ";
    passIssuedCode.value = "НЕ ЗАПОЛНЯЕТСЯ";
  }

  if (value === "ЗАО") {
    companyName.value = "";
    registrationAddr.value = "НЕ ЗАПОЛНЯЕТСЯ";
    posPerAcc.value = "";
    positionNom.value = "";
    actingOn.value = "";
    legalAddr.value = "";
    postalAddr.readonly = "";
    kpp.value = "";
    ogrn.value = "";
    okpo.value = "";
    passportSeries.value = "НЕ ЗАПОЛНЯЕТСЯ";
    passportNumber.value = "НЕ ЗАПОЛНЯЕТСЯ";
    passIssuedBy.value = "НЕ ЗАПОЛНЯЕТСЯ";
    passIssuedDate.value = "НЕ ЗАПОЛНЯЕТСЯ";
    passIssuedCode.value = "НЕ ЗАПОЛНЯЕТСЯ";
  }

  if (value === "АО") {
    companyName.value = "";
    registrationAddr.value = "НЕ ЗАПОЛНЯЕТСЯ";
    posPerAcc.value = "";
    positionNom.value = "";
    actingOn.value = "";
    legalAddr.value = "";
    postalAddr.readonly = "";
    kpp.value = "";
    ogrn.value = "";
    okpo.value = "";
    passportSeries.value = "НЕ ЗАПОЛНЯЕТСЯ";
    passportNumber.value = "НЕ ЗАПОЛНЯЕТСЯ";
    passIssuedBy.value = "НЕ ЗАПОЛНЯЕТСЯ";
    passIssuedDate.value = "НЕ ЗАПОЛНЯЕТСЯ";
    passIssuedCode.value = "НЕ ЗАПОЛНЯЕТСЯ";
  }

  if (value === "ОАО") {
    companyName.value = "";
    registrationAddr.value = "НЕ ЗАПОЛНЯЕТСЯ";
    posPerAcc.value = "";
    positionNom.value = "";
    actingOn.value = "";
    legalAddr.value = "";
    postalAddr.readonly = "";
    kpp.value = "";
    ogrn.value = "";
    okpo.value = "";
    passportSeries.value = "НЕ ЗАПОЛНЯЕТСЯ";
    passportNumber.value = "НЕ ЗАПОЛНЯЕТСЯ";
    passIssuedBy.value = "НЕ ЗАПОЛНЯЕТСЯ";
    passIssuedDate.value = "НЕ ЗАПОЛНЯЕТСЯ";
    passIssuedCode.value = "НЕ ЗАПОЛНЯЕТСЯ";
  }

  if (value === "ИП") {
    companyName.value = "НЕ ЗАПОЛНЯЕТСЯ";
    registrationAddr.value = "";
    posPerAcc.value = "НЕ ЗАПОЛНЯЕТСЯ";
    positionNom.value = "НЕ ЗАПОЛНЯЕТСЯ";
    actingOn.value = "НЕ ЗАПОЛНЯЕТСЯ";
    legalAddr.value = "НЕ ЗАПОЛНЯЕТСЯ";
    postalAddr.readonly = "";
    kpp.value = "НЕ ЗАПОЛНЯЕТСЯ";
    ogrn.value = "";
    okpo.value = "";
    passportSeries.value = "НЕ ЗАПОЛНЯЕТСЯ";
    passportNumber.value = "НЕ ЗАПОЛНЯЕТСЯ";
    passIssuedBy.value = "НЕ ЗАПОЛНЯЕТСЯ";
    passIssuedDate.value = "НЕ ЗАПОЛНЯЕТСЯ";
    passIssuedCode.value = "НЕ ЗАПОЛНЯЕТСЯ";
  }

  if (value === "Физлицо") {
    companyName.value = "НЕ ЗАПОЛНЯЕТСЯ";
    registrationAddr.value = "";
    posPerAcc.value = "НЕ ЗАПОЛНЯЕТСЯ";
    positionNom.value = "НЕ ЗАПОЛНЯЕТСЯ";
    actingOn.value = "НЕ ЗАПОЛНЯЕТСЯ";
    legalAddr.value = "НЕ ЗАПОЛНЯЕТСЯ";
    postalAddr.readonly = "";
    kpp.value = "НЕ ЗАПОЛНЯЕТСЯ";
    ogrn.value = "НЕ ЗАПОЛНЯЕТСЯ";
    okpo.value = "НЕ ЗАПОЛНЯЕТСЯ";
    passportSeries.value = "";
    passportNumber.value = "";
    passIssuedBy.value = "";
    passIssuedDate.value = "";
    passIssuedCode.value = "";
  }

});