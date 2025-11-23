export type StatusState = "idle" | "saving" | "success" | "error";

export interface WifiBody {
  ssid: string;
  psk?: string;
}

export interface WifiStatusResponse {
  configured: boolean;
  ssid: string | null;
  pskSet: boolean;
}
