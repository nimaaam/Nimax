document.getElementById("buyBtn").addEventListener("click", () => {
  const ticketCode = "HN-" + Math.floor(Math.random() * 100000);
  document.getElementById("ticketResult").innerText =
    `✅ بلیط شما صادر شد: ${ticketCode}`;
});