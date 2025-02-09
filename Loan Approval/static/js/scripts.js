function loadDemoData() {
    fetch('../static/js/demo.json')
        .then(res => res.json())
        .then(data => {
            // console.table(data.demos[demo_no])
            let demo_no =document.getElementById('select').value
            let selected = data.demos[demo_no]
            document.getElementById('no_of_dependents').value = selected[' no_of_dependents']
            document.getElementById('no_of_dependents_o').value = selected[' no_of_dependents']
            document.getElementById('income_annum').value = (selected[' income_annum'] / 1000)
            document.getElementById('loan_amount').value = (selected[' loan_amount'] / 1000)
            document.getElementById('loan_term').value = selected[' loan_term']
            document.getElementById('cibil_score').value = selected[' cibil_score']
            document.getElementById('residential_assets_value').value = (selected[' residential_assets_value'] / 1000)
            document.getElementById('commercial_assets_value').value = (selected[' commercial_assets_value'] / 1000)
            document.getElementById('luxury_assets_value').value = (selected[' luxury_assets_value'] / 1000)
            document.getElementById('bank_asset_value').value = (selected[' bank_asset_value'] / 1000)
            if (selected[' self_employed'] == ' Yes') {
                document.getElementById('self_employed_yes').checked = true
            }
            else {
                document.getElementById('self_employed_no').checked = true
            }
            if (selected[' education'] == ' Graduate') {
                document.getElementById('graduated').checked = true
            }
            else {
                document.getElementById('ngraduated').checked = true
            }


        })
}