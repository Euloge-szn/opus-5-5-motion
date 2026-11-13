import { Composition } from "remotion";
import { MaVideo } from "./MaVideo";

// Chaque <Composition> est une vidéo qu'on voit dans Remotion Studio.
// Pour en ajouter une, demande simplement à Claude.
export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="MaVideo"
        component={MaVideo}
        durationInFrames={150}
        fps={30}
        width={1080}
        height={1920}
      />
    </>
  );
};
