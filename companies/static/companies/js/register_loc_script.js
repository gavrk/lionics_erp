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
  companyName.disabled = true;
  posPerAcc.disabled = true;
  positionNom.disabled = true;
  actingOn.disabled = true;
  legalAddr.disabled = true;
  registrationAddr.disabled = true;
  kpp.disabled = true;
  ogrn.disabled = true;
  okpo.disabled = true;
  passportSeries.disabled = true;
  passportNumber.disabled = true;
  passIssuedBy.disabled = true;
  passIssuedDate.disabled = true;
  passIssuedCode.disabled = true;


  if (value === "ООО") {
    companyName.disabled = false;
    posPerAcc.disabled = false;
    positionNom.disabled = false;
    actingOn.disabled = false;
    legalAddr.disabled = false;
    kpp.disabled = false;
    ogrn.disabled = false;
    okpo.disabled = false;
  }

  if (value === "ЗАО") {
    companyName.disabled = false;
    posPerAcc.disabled = false;
    positionNom.disabled = false;
    actingOn.disabled = false;
    legalAddr.disabled = false;
    kpp.disabled = false;
    ogrn.disabled = false;
    okpo.disabled = false;
  }

  if (value === "АО") {
    companyName.disabled = false;
    posPerAcc.disabled = false;
    positionNom.disabled = false;
    actingOn.disabled = false;
    legalAddr.disabled = false;
    kpp.disabled = false;
    ogrn.disabled = false;
    okpo.disabled = false;
  }

  if (value === "ОАО") {
    companyName.disabled = false;
    posPerAcc.disabled = false;
    positionNom.disabled = false;
    actingOn.disabled = false;
    legalAddr.disabled = false;
    kpp.disabled = false;
    ogrn.disabled = false;
    okpo.disabled = false;
  }

  if (value === "ИП") {
    registrationAddr.disabled = false;
    ogrn.disabled = false;
    okpo.disabled = false;
  }

  if (value === "Физлицо") {
    registrationAddr.disabled = false;
    passportSeries.disabled = false;
    passportNumber.disabled = false;
    passIssuedBy.disabled = false;
    passIssuedDate.disabled = false;
    passIssuedCode.disabled = false;
  }

});