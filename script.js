function calculateEfficiency() {
    // Get the input values from OC and SC tests
    const P_OC = parseFloat(document.getElementById('ocPower').value);
    const P_SC = parseFloat(document.getElementById('scPower').value);
    const loadPower = parseFloat(document.getElementById('loadPower').value);
    const loadFactor = parseFloat(document.getElementById('loadFactor').value);

    // Validate inputs
    if (isNaN(P_OC) || isNaN(P_SC) || isNaN(loadPower) || isNaN(loadFactor)) {
        alert("Please enter valid numbers for all fields.");
        return;
    }

    if (P_OC < 0 || P_SC < 0 || loadPower < 0 || loadFactor < 0 || loadFactor > 1) {
        alert("Power values must be non-negative and load factor should be between 0 and 1.");
        return;
    }

    // Copper losses at full load from SC test (P_SC)
    // At fractional load, copper losses scale with square of load factor
    const copperLosses = P_SC * loadFactor * loadFactor;

    // Core losses are constant, as determined from OC test (P_OC)
    const coreLosses = P_OC;

    // Total losses
    const totalLosses = copperLosses + coreLosses;

    // Input power is the sum of output power and total losses
    const inputPower = loadPower + totalLosses;

    // Efficiency calculation
    const efficiency = (loadPower / inputPower) * 100;
    const remark=(efficiency > 80 )? "Good" : (efficiency >50) ? "Average": "Poor";

    // Display result
    document.getElementById('result').textContent = `Transformer Efficiency: ${efficiency.toFixed(2)}%`;
    document.getElementById('remark').textContent= remark;
    document.getElementById('remark').style.color=(efficiency > 80 )? "Green" : (efficiency >50) ? "brown": "Red";

    // Display explanation card
    const explanationCard = document.getElementById('explanationCard');
    explanationCard.classList.remove('hidden');

    // Set explanation text
    const explanationText = `
    <ul>
        <li><strong>Core Losses (P_OC):</strong> These are obtained from the open circuit test and are constant regardless of load.
            <br>In this case, P_OC = ${P_OC} W.
        </li>
        <li><strong>Copper Losses (P_SC):</strong> These losses are obtained from the short circuit test and vary with load.
            <br>At the given load factor (x = ${loadFactor}), the copper losses are 
            <br>P_Cu = P_SC * x<sup>2</sup> = ${P_SC} * ${loadFactor}<sup>2</sup> = ${copperLosses.toFixed(2)} W.
        </li>
        <li><strong>Total Losses:</strong> The total losses are the sum of core and copper losses:
            <br>Total Losses = ${coreLosses.toFixed(2)} W + ${copperLosses.toFixed(2)} W = ${totalLosses.toFixed(2)} W.
        </li>
        <li><strong>Input Power:</strong> The input power is the sum of the output power and total losses:
            <br>Input Power = ${loadPower} W + ${totalLosses.toFixed(2)} W = ${inputPower.toFixed(2)} W.
        </li>
        <li><strong>Efficiency (η):</strong> Efficiency is calculated as the ratio of output power to input power, expressed as a percentage:
            <br>η = (Output Power / Input Power) * 100 = (${loadPower} / ${inputPower.toFixed(2)}) * 100 = ${efficiency.toFixed(2)} %.
        </li>
    </ul>
`;
    document.getElementById('explanationText').innerHTML = explanationText;

}
