// TTS Player for mdBook — Bulgarian audiobook reader
// Injected globally via book.toml additional-js
(function() {
  if (!window.speechSynthesis) return;

  const synth = window.speechSynthesis;
  let utterance = null;
  let paragraphs = [];
  let currentIdx = 0;
  let isPaused = false;
  let voices = [];
  let started = false;

  // Build the UI
  const container = document.createElement('div');
  container.id = 'tts-controls';
  container.innerHTML = `
    <div class="tts-bar">
      <button id="ttsPlay" title="Слушай">▶</button>
      <button id="ttsPause" title="Пауза" disabled>⏸</button>
      <button id="ttsStop" title="Стоп" disabled>⏹</button>
      <select id="ttsVoice"></select>
      <div class="tts-speed">
        <input type="range" id="ttsRate" min="0.5" max="2" step="0.1" value="1">
        <span id="ttsRateVal">1.0x</span>
      </div>
      <span id="ttsStatus" class="tts-status"></span>
    </div>
  `;

  const style = document.createElement('style');
  style.textContent = `
    #tts-controls { position: sticky; top: 0; z-index: 100; margin: 0 0 20px 0; }
    .tts-bar {
      display: flex; flex-wrap: wrap; align-items: center; gap: 8px;
      padding: 10px 14px; border-radius: 8px;
      background: var(--sidebar-bg, #292c2f); border: 1px solid var(--sidebar-separator, #3a3a3a);
      font-size: 14px;
    }
    .tts-bar button {
      background: var(--links, #4e8bda); color: white; border: none;
      padding: 6px 14px; border-radius: 6px; cursor: pointer; font-size: 15px;
    }
    .tts-bar button:hover { opacity: 0.85; }
    .tts-bar button:disabled { opacity: 0.3; cursor: not-allowed; }
    .tts-bar button#ttsStop { background: #c0392b; }
    .tts-bar select {
      background: var(--theme-popup-bg, #222); color: var(--fg, #ddd);
      border: 1px solid var(--sidebar-separator, #444); padding: 5px 8px; border-radius: 6px; font-size: 13px;
      max-width: 200px;
    }
    .tts-speed { display: flex; align-items: center; gap: 4px; }
    .tts-speed input { width: 70px; }
    .tts-speed span { font-size: 12px; color: var(--sidebar-fg, #999); min-width: 30px; }
    .tts-status { font-size: 12px; color: var(--sidebar-fg, #999); margin-left: auto; }
    .tts-highlight { background: rgba(78,139,218,0.15); border-radius: 3px; }
    @media (max-width: 600px) {
      .tts-bar { gap: 6px; padding: 8px 10px; }
      .tts-bar select { max-width: 120px; font-size: 12px; }
    }
  `;
  document.head.appendChild(style);

  // Insert into mdBook content area
  function insertControls() {
    const content = document.getElementById('content') || document.querySelector('.content');
    if (!content) return;
    const main = content.querySelector('main') || content;
    if (main.firstChild) {
      main.insertBefore(container, main.firstChild);
    } else {
      main.appendChild(container);
    }
  }

  function populateVoices() {
    voices = synth.getVoices();
    const select = document.getElementById('ttsVoice');
    if (!select) return;
    select.innerHTML = '';

    const bgVoices = voices.filter(v => v.lang && v.lang.startsWith('bg'));

    if (bgVoices.length === 0) {
      const opt = document.createElement('option');
      opt.textContent = 'Няма BG глас — вижте настройки';
      opt.value = '';
      select.appendChild(opt);
      const st = document.getElementById('ttsStatus');
      if (st) st.textContent = 'Инсталирайте български глас от настройките на устройството';
    } else {
      bgVoices.forEach((v, i) => {
        const opt = document.createElement('option');
        opt.value = voices.indexOf(v);
        opt.textContent = '🇧🇬 ' + v.name;
        if (i === 0) opt.selected = true;
        select.appendChild(opt);
      });
      const st = document.getElementById('ttsStatus');
      if (st) st.textContent = '🔈 Готово';
    }
  }

  function getParagraphs() {
    const content = document.getElementById('content') || document.querySelector('.content');
    if (!content) return [];
    return Array.from(content.querySelectorAll('p, h1, h2, h3, h4, blockquote, li'))
      .filter(el => !el.closest('#tts-controls'));
  }

  function highlight(el) {
    document.querySelectorAll('.tts-highlight').forEach(e => e.classList.remove('tts-highlight'));
    if (el) {
      el.classList.add('tts-highlight');
      el.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }
  }

  function speakNext() {
    if (currentIdx >= paragraphs.length) {
      stopReading();
      const st = document.getElementById('ttsStatus');
      if (st) st.textContent = 'Край на главата';
      return;
    }

    const el = paragraphs[currentIdx];
    const text = el.textContent.trim();
    if (!text) { currentIdx++; speakNext(); return; }

    highlight(el);

    utterance = new SpeechSynthesisUtterance(text);

    const voiceIdx = document.getElementById('ttsVoice').value;
    if (voiceIdx !== '' && voices[voiceIdx]) {
      utterance.voice = voices[voiceIdx];
      utterance.lang = voices[voiceIdx].lang;
    } else {
      utterance.lang = 'bg-BG';
    }

    utterance.rate = parseFloat(document.getElementById('ttsRate').value);
    utterance.pitch = 1;

    utterance.onend = function() {
      currentIdx++;
      speakNext();
    };

    utterance.onerror = function(e) {
      if (e.error !== 'canceled' && e.error !== 'interrupted') {
        const st = document.getElementById('ttsStatus');
        if (st) st.textContent = 'Грешка: ' + e.error;
      }
    };

    const st = document.getElementById('ttsStatus');
    if (st) st.textContent = (currentIdx + 1) + ' / ' + paragraphs.length;
    synth.speak(utterance);
  }

  function startReading() {
    synth.cancel();
    paragraphs = getParagraphs();
    currentIdx = 0;
    isPaused = false;
    started = true;

    document.getElementById('ttsPlay').disabled = true;
    document.getElementById('ttsPause').disabled = false;
    document.getElementById('ttsStop').disabled = false;
    document.getElementById('ttsPause').textContent = '⏸';

    speakNext();
  }

  function togglePause() {
    if (isPaused) {
      synth.resume();
      isPaused = false;
      document.getElementById('ttsPause').textContent = '⏸';
    } else {
      synth.pause();
      isPaused = true;
      document.getElementById('ttsPause').textContent = '▶';
    }
  }

  function stopReading() {
    synth.cancel();
    isPaused = false;
    started = false;
    highlight(null);

    document.getElementById('ttsPlay').disabled = false;
    document.getElementById('ttsPause').disabled = true;
    document.getElementById('ttsStop').disabled = true;
    document.getElementById('ttsPause').textContent = '⏸';
  }

  // Click paragraph to jump
  function handleContentClick(e) {
    if (!started) return;
    const p = e.target.closest('p, h1, h2, h3, h4, blockquote, li');
    if (!p || p.closest('#tts-controls')) return;
    const idx = paragraphs.indexOf(p);
    if (idx >= 0) {
      synth.cancel();
      currentIdx = idx;
      isPaused = false;
      document.getElementById('ttsPlay').disabled = true;
      document.getElementById('ttsPause').disabled = false;
      document.getElementById('ttsStop').disabled = false;
      document.getElementById('ttsPause').textContent = '⏸';
      speakNext();
    }
  }

  // Init
  insertControls();

  document.getElementById('ttsPlay').addEventListener('click', startReading);
  document.getElementById('ttsPause').addEventListener('click', togglePause);
  document.getElementById('ttsStop').addEventListener('click', stopReading);
  document.getElementById('ttsRate').addEventListener('input', function() {
    document.getElementById('ttsRateVal').textContent = this.value + 'x';
  });

  const content = document.getElementById('content') || document.querySelector('.content');
  if (content) content.addEventListener('click', handleContentClick);

  synth.onvoiceschanged = populateVoices;
  populateVoices();
  // Some browsers need a delay
  setTimeout(populateVoices, 500);
})();
