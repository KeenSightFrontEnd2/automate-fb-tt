import { useState } from "react";
import axios from "axios";

const baseURL = "http://localhost:5000/api";

const App = () => {
  const [facebookMessage, setFacebookMessage] = useState("");
  const [tiktokMessage, setTiktokMessage] = useState("");
  const [tiktokVideoUrl, setTiktokVideoUrl] = useState("");
  const [marketplaceTitle, setMarketplaceTitle] = useState("");
  const [marketplacePrice, setMarketplacePrice] = useState("");
  const [marketplaceDescription, setMarketplaceDescription] = useState("");
  const [marketplaceImageUrl, setMarketplaceImageUrl] = useState("");
  const [tiktokMarketplaceTitle, setTiktokMarketplaceTitle] = useState("");
  const [tiktokMarketplaceVideoUrl, setTiktokMarketplaceVideoUrl] = useState("");

  const handlePostFacebook = () => {
    axios
      .post(`${baseURL}/post_facebook`, { message: facebookMessage })
      .then((response) => alert("Posted to Facebook: " + response.data.status))
      .catch((error) => console.error("Error posting to Facebook:", error));
  };

  const handlePostTikTok = () => {
    axios
      .post(`${baseURL}/post_tiktok`, { message: tiktokMessage, video_url: tiktokVideoUrl })
      .then((response) => alert("Posted to TikTok: " + response.data.status))
      .catch((error) => console.error("Error posting to TikTok:", error));
  };

  const handlePostFacebookMarketplace = () => {
    axios
      .post(`${baseURL}/post_facebook_marketplace`, {
        title: marketplaceTitle,
        price: marketplacePrice,
        description: marketplaceDescription,
        image_url: marketplaceImageUrl,
      })
      .then((response) => alert("Posted to Facebook Marketplace: " + response.data.status))
      .catch((error) => console.error("Error posting to Facebook Marketplace:", error));
  };

  const handlePostTikTokMarketplace = () => {
    axios
      .post(`${baseURL}/post_tiktok_marketplace`, {
        title: tiktokMarketplaceTitle,
        video_url: tiktokMarketplaceVideoUrl,
      })
      .then((response) => alert("Posted to TikTok Marketplace: " + response.data.status))
      .catch((error) => console.error("Error posting to TikTok Marketplace:", error));
  };

  const handleFacebookLogin = () => {
    window.location.href = "http://localhost:5000/api/login/facebook";
  };

  const handleTikTokLogin = () => {
    window.location.href = "http://localhost:5000/api/login/tiktok";
  };

  return (
    <main>
      <h1>Social Media Automation</h1>
      
      <div className="login">
        <button onClick={handleFacebookLogin}>Login with Facebook</button>
        <button onClick={handleTikTokLogin}>Login with TikTok</button>
      </div>

      <div className="parts">
        <h2>Post to Facebook</h2>
        <textarea
          value={facebookMessage}
          onChange={(e) => setFacebookMessage(e.target.value)}
          placeholder="Message"
        />
        <br />
        <button onClick={handlePostFacebook}>Post to Facebook</button>
      </div>

      <div className="parts">
        <h2>Post to TikTok</h2>
        <textarea
          value={tiktokMessage}
          onChange={(e) => setTiktokMessage(e.target.value)}
          placeholder="Message"
        />
        <br />
        <input
          type="text"
          value={tiktokVideoUrl}
          onChange={(e) => setTiktokVideoUrl(e.target.value)}
          placeholder="Video URL"
        />
        <br />
        <button onClick={handlePostTikTok}>Post to TikTok</button>
      </div>

      <div className="parts">
        <h2>Post to Facebook Marketplace</h2>
        <input
          type="text"
          value={marketplaceTitle}
          onChange={(e) => setMarketplaceTitle(e.target.value)}
          placeholder="Title"
        />
        <br />
        <input
          type="text"
          value={marketplacePrice}
          onChange={(e) => setMarketplacePrice(e.target.value)}
          placeholder="Price"
        />
        <br />
        <textarea
          value={marketplaceDescription}
          onChange={(e) => setMarketplaceDescription(e.target.value)}
          placeholder="Description"
        />
        <br />
        <input
          type="text"
          value={marketplaceImageUrl}
          onChange={(e) => setMarketplaceImageUrl(e.target.value)}
          placeholder="Image URL"
        />
        <br />
        <button onClick={handlePostFacebookMarketplace}>Post to Facebook Marketplace</button>
      </div>

      <div className="parts">
        <h2>Post to TikTok Marketplace</h2>
        <input
          type="text"
          value={tiktokMarketplaceTitle}
          onChange={(e) => setTiktokMarketplaceTitle(e.target.value)}
          placeholder="Title"
        />
        <br />
        <input
          type="text"
          value={tiktokMarketplaceVideoUrl}
          onChange={(e) => setTiktokMarketplaceVideoUrl(e.target.value)}
          placeholder="Video URL"
        />
        <br />
        <button onClick={handlePostTikTokMarketplace}>Post to TikTok Marketplace</button>
      </div>
    </main>
  );
};

export default App;
