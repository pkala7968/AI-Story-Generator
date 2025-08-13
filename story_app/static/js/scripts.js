document.addEventListener("DOMContentLoaded", function () {
    const micBtn = document.getElementById('mic-btn');
    const promptEl = document.getElementById('prompt');

    if (!micBtn || !promptEl) {
        console.error("❌ mic-btn or prompt element not found in DOM.");
        return;
    }

    micBtn.addEventListener('click', function () {
        // Browser SpeechRecognition API (Chrome / Brave)
        window.SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
        const recognition = new SpeechRecognition();

        recognition.interimResults = true;
        recognition.continuous = true; // keep listening until stopped

        let silenceTimer;

        recognition.addEventListener('result', e => {
            const transcript = Array.from(e.results)
                .map(result => result[0])
                .map(result => result.transcript)
                .join('');

            console.log("🎤 Transcript:", transcript);
            promptEl.value = transcript;

            // Reset silence timer when speech is detected
            clearTimeout(silenceTimer);
            silenceTimer = setTimeout(() => {
                console.log("⏹ Stopping due to 5s silence...");
                recognition.stop();
            }, 5000);
        });

        recognition.addEventListener('error', e => {
            console.error("SpeechRecognition error:", e);
        });

        recognition.addEventListener('end', () => {
            clearTimeout(silenceTimer);
            console.log("Speech recognition ended.");
        });

        // Start recognition
        console.log("🎙 Listening...");
        recognition.start();

        // Initial silence timeout (if no speech from start)
        silenceTimer = setTimeout(() => {
            console.log("⏹ No speech detected in 5s. Stopping...");
            recognition.stop();
        }, 5000);
    });
});